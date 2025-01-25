import { expect } from "jsr:@std/expect";
import { Hono } from "hono";
import { testClient } from "hono/testing";

Deno.test("GET /books", async () => {
	const app = new Hono().get("/books", (c) => c.json([]));
	const res = await testClient(app).books.$get();
	expect(res.status).toEqual(200);
	expect(await res.json()).toEqual([]);
});

Deno.test("POST /book", async () => {
	const app = new Hono().post(
		"/book",
		(c) =>
			c.json(`Successfully added "Test book" to your library.`, 201, {
				"Content-Type": "text/plain",
			}),
	);
	const res = await testClient(app).book.$post();
	expect(res.status).toEqual(201);
	expect(await res.json()).toEqual(
		`Successfully added "Test book" to your library.`,
	);
});
