import { Hono } from "hono";
import { logger } from "hono/logger";
import mongoose from "mongoose";
import { bookRouter } from "./routes/book.router.ts";

const app = new Hono();

app.use(logger());
const PORT = parseInt(Deno.env.get("PORT")!) || undefined;

const MONGODB_URI = Deno.env.get("MONGODB_URI") || "";
const DB_NAME = "libraries";

await mongoose.connect(`${MONGODB_URI}/${DB_NAME}`);
console.log("MONGOOSE:", mongoose.connection.readyState);

app.route("/api", bookRouter);

Deno.serve({ port: PORT }, app.fetch);
