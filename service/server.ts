import { Hono } from "@hono/hono"

const app = new Hono()

app.get("/", (c) => {
	return c.text("New deno project")
})

Deno.serve(app.fetch);
