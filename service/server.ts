import { Hono } from "@hono/hono";
import { homeLibrary } from "./db/db.ts";

const app = new Hono();

app.get("/", (c) => {
	return c.text("New deno project");
});

app.get("/books", async (c) => {
	const books = await homeLibrary.find().toArray();
	return c.json(books);
});

Deno.serve(app.fetch);
