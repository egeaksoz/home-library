import { Context } from "hono";
import Book from "../models/book.ts";

async function getBooks(c: Context): Promise<Response> {
	return c.json(await Book.find());
}

async function addBook(c: Context): Promise<Response> {
	const book = await Book.create(await c.req.json());
	return c.body(`Successfully added "${book.title}" to your library.`, 201, {
		"Content-Type": "text/plain",
	});
}

export { addBook, getBooks };
