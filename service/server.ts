import { Context, Hono } from "@hono/hono";
import { addBook, getBooks } from "./controllers/bookController.ts";

const app = new Hono();
const PORT = parseInt(Deno.env.get("PORT")!) || undefined;

app.get("/books", async (c: Context) => {
	return await getBooks(c);
});

app.post("/books", async (c: Context) => {
	return await addBook(c);
});

Deno.serve({ port: PORT }, app.fetch);
