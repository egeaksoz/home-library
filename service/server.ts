import { Context, Hono } from "@hono/hono";
import { homeLibrary } from "./db/db.ts";

const app = new Hono();
const PORT = parseInt(Deno.env.get("PORT")!) || undefined;

app.get("/", (c: Context) => {
	return c.text("New deno project");
});

app.get("/books", async (c: Context) => {
	const books = await homeLibrary.find().toArray();
	return c.json(books);
});

app.post("/books", async (c: Context) => {
	const book = await c.req.json();
	await homeLibrary.insertOne(book);
	return c.body(`Successfully added "${book.title}" to your library.`, 201, {
		"Content-Type": "text/plain",
	});
});

Deno.serve({ port: PORT }, app.fetch);
