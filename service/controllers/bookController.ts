import { Context } from "@hono/hono";
import { homeLibrary } from "../db/db.ts";

async function getBooks(c: Context): Promise<Response> {
	return c.json(await homeLibrary.find().toArray());
}

async function addBook(c: Context): Promise<Response> {
	const book = await c.req.json();
	await homeLibrary.insertOne(book);
	return c.body(`Successfully added "${book.title}" to your library.`, 201, {
		"Content-Type": "text/plain",
	});
}

export { addBook, getBooks };
