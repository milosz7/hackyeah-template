#### Running the containers
1. Open a terminal session inside the project root directory and run
```bash
docker-compose up --build
```
2. Open vscode and click the left-bottom corner icon.
3. From the dropdown select "Attach to a running container".
4. Open frontend/backend container.
5. Expand the `Explorer` tab and move to `/usr/src/app` directory.
6. Repeat above steps for the remaining container.
7. Frontend is hosted on port `4200` and the backend is hosted on `8080`.
