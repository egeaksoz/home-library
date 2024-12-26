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

Deno.serve({ port: PORT }, app.fetch);
