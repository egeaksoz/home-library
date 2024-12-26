import { Hono } from "@hono/hono";
import { homeLibrary } from "./db/db.ts";

const app = new Hono();
const PORT = Deno.env.get("PORT") || "3001";

app.get("/", (c) => {
	return c.text("New deno project");
});

app.get("/books", async (c) => {
	const books = await homeLibrary.find().toArray();
	return c.json(books);
});

Deno.serve({ port: PORT }, app.fetch);
