# Browser Fingerprinting

Examples of various approaches to browser fingerprinting.

## Client Examples

The client examples consist of just a `index.html` file. You can either just open the file in the browser or serve the file via a lightweight HTTP server.

To serve the file, first change into the appropriate directory and then

```bash
python3 -m http.server 8000
```

## Server Examples

The server examples use FastAPI and need to be run via a server.

To launch a server, first change into the appropriate directory and then

```
uvicorn main:app --reload
```
