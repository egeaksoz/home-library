import { MongoClient } from "npm:mongodb@6.12.0";

const MONGODB_URI = Deno.env.get("MONGODB_URI") || "";
const DB_NAME = "libraries";

if (!MONGODB_URI) {
	console.error("MONGODB_URI is not set");
	Deno.exit(1);
}

const client = new MongoClient(MONGODB_URI);

try {
	await client.connect();
	await client.db("admin").command({ ping: 1 });
	console.log("Connected to MongoDB");
} catch (error) {
	console.error("Error connecting to MongoDb", error);
	Deno.exit(1);
}

const db = client.db(DB_NAME);
const homeLibrary = db.collection("home");

export { db, homeLibrary };
