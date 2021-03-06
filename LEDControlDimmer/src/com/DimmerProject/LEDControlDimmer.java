package com.DimmerProject;

import com.mongodb.Block;

import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.*;
import org.bson.Document;

import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;
import net.sourceforge.jFuzzyLogic.plot.JFuzzyChart;
import net.sourceforge.jFuzzyLogic.rule.Variable;
import net.sourceforge.jFuzzyLogic.rule.Rule;


import java.util.ArrayList;
import java.util.List;

public class LEDControlDimmer {
	public static void main(String[] args) throws Exception{

		MongoClient mongoClient = new MongoClient();
		MongoDatabase db = mongoClient.getDatabase("Sensors");
	    System.out.println("Connected to database successfully");
		
	    
	    MongoCollection<Document> collection = db.getCollection("ambientlight");
	    MongoCursor<Document> cursor= collection.find().iterator();
	    //try{
	    	//while(cursor.hasNext()){
	    		//System.out.println(cursor.next().toJson());
	    	//}
	   // } finally{
	    //	cursor.close();
	    //}
	    //for (Document cur : collection.find()){
	    	//System.out.println(cur.toJson());
	    //}
	    
	    //TODO: query lux value from db every 10 minutes and feed into controller; feed value 0 to controller if no occupancy for 10min
	 
	   // Document lux = collection.find().first();
	    //lux = collection.find(gt("lux", 0)).first();

	    //System.out.println(lux.toJson());
	    
		//load from FCL file
		String fileName = "Dimmer.fcl";
		FIS fis = FIS.load(fileName, true);
		if(fis == null){
			System.err.println("can't load file: '" +fileName + "'");
			return;
		}
		
		//show ruleset
		FunctionBlock functionBlock = fis.getFunctionBlock(null);
		//functionBlock.chart();
		
		JFuzzyChart.get().chart(functionBlock);
		
		//comment below, used for testing purposes.
		//set inputs
		//for (int i=0; i<=1500; i+=100){
			//fis.setVariable("AmbientLight",i);
			//fis.setVariable("Occupancy", 1);
			//fis.setVariable("TargetLux", 800);
			//functionBlock.evaluate();
			//Variable LED = functionBlock.getVariable("LEDOutput");
			//JFuzzyChart.get().chart(LED, LED.getDefuzzifier(), true);
			//double LED_OUTPUT = fis.getVariable("LEDOutput").getValue();
			//System.out.println("Average LED Output at " +i+ " is " +(int)Math.round(LED_OUTPUT));
			//System.out.println(i+ "," +(int)Math.round(LED_OUTPUT));
			//for( Rule r : fis.getFunctionBlock("Dimmer").getFuzzyRuleBlock("rules").getRules() )
			//    System.out.println(r);
	        //System.out.println();
		}
		
		for( Rule r : fis.getFunctionBlock("Dimmer").getFuzzyRuleBlock("rules").getRules() )
			     System.out.println(r);
		//evaluate
		functionBlock.evaluate();
		Variable LED = functionBlock.getVariable("LEDOutput");
		
		show output variables chart
		JFuzzyChart.get().chart(LED, LED.getDefuzzifier(), true);
		
		System.out.println(fis);
		double LED_OUTPUT = fis.getVariable("LEDOutput").getValue();
		System.out.println("Average LED Output: " +(int)Math.round(LED_OUTPUT));
		
	}
}
