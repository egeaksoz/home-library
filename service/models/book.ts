import { model, Schema } from "npm:mongoose@^6.7";

const bookSchema = new Schema({
	title: String,
	author: String,
	language: String,
	genre: String,
	cover: String,
	read: Boolean,
	description: String,
});

const Book = model("Book", bookSchema);
export default Book;
