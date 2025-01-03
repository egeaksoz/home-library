import { model, Schema } from "mongoose";

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
