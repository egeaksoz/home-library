Deno.serve({ port: 3000 }, (_req) => {
	return new Response("New deno project");
});
