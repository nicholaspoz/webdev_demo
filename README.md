# Flask Server Examples

Install Flask (and other dependencies)

```
$ pip install -r requirements.txt
```

### Example 1: Get a server running

Two endpoints:

- `GET /` that says Hello World
- `GET /say-hello/<input>` that returns JSON with a message

```
$ ./start example_1
```

### Example 2: Application State (in memory)

There is an `/increment` and `/reset` endpoint that change a counter in the server's memory.

Restarting the server resets the counter.

```
$ ./start example_1
```

### Example 3: Persistent Application State

There are the same endpoints as before, except now we're using a database to store the counters.

The counter is preserved after restarting the server.

```
$ ./start example_3
```
