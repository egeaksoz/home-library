import { Hono } from "hono";
import { getBooks } from "../controllers/bookController.ts";
import { addBook } from "../controllers/bookController.ts";

const bookRouter = new Hono();

bookRouter.get("/books", (c) => getBooks(c));
bookRouter.post("/book", (c) => addBook(c));

export { bookRouter };
