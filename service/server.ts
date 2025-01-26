import { Context, Hono } from "hono";
import { logger } from "hono/logger";
import { addBook, getBooks } from "./controllers/bookController.ts";
import mongoose from "mongoose";

const app = new Hono();

app.use(logger());
const PORT = parseInt(Deno.env.get("PORT")!) || undefined;

const MONGODB_URI = Deno.env.get("MONGODB_URI") || "";
const DB_NAME = "libraries";

await mongoose.connect(`${MONGODB_URI}/${DB_NAME}`);
console.log("MONGOOSE:", mongoose.connection.readyState);

app.get("/books", async (c: Context) => {
	return await getBooks(c);
});

app.post("/books", async (c: Context) => {
	return await addBook(c);
});

Deno.serve({ port: PORT }, app.fetch);
