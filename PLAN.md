# Todo App Plan

FastAPI backend + Expo (React Native) mobile frontend, in one monorepo.

## Target structure

```
todo/
├── backend/          # FastAPI (move pyproject.toml, .python-version, src/ here)
│   ├── pyproject.toml
│   └── src/todo/
│       ├── main.py       # app + router wiring
│       ├── database.py   # engine + session
│       ├── models.py     # SQLModel tables/schemas
│       └── routes.py     # endpoints
├── mobile/           # Expo React Native app
├── .gitignore
├── PLAN.md
└── README.md
```

## Phase 0: Prep
- [ ] Move the existing Python files into `backend/` and make the first commit
- [ ] Install Node (LTS) and Expo Go on your phone

## Phase 1: Backend
- [ ] **Hello world.** `uv add "fastapi[standard]" sqlmodel`. In `main.py`, create `app = FastAPI()` and one `GET /` route returning `{"status": "ok"}`. Run `uv run fastapi dev`, open `http://localhost:8000/docs`.
  *Concepts: decorators, path operations, auto-generated docs.*
- [ ] **Model.** In `models.py`, define `Todo` with `id`, `title`, `done`, `created_at`.
  *Concepts: SQLModel `table=True`, type hints, Pydantic validation.*
- [ ] **Database.** In `database.py`, create a SQLite engine, a function that creates tables on startup, and a `get_session` dependency.
  *Concepts: engine vs session, FastAPI `Depends`, lifespan events.*
- [ ] **Separate schemas.** Define `TodoCreate`, `TodoUpdate`, `TodoRead` so clients can't set the `id`.
  *Concepts: why you don't expose your table model directly.*
- [ ] **CRUD endpoints.** In `routes.py` use an `APIRouter`, include it in `main.py`:
  - `POST /todos`
  - `GET /todos`
  - `GET /todos/{id}`
  - `PATCH /todos/{id}`
  - `DELETE /todos/{id}`

  Return 404 when not found (`HTTPException`).
- [ ] **Test.** Write tests in `tests/` with `pytest` and `TestClient`, using an in-memory SQLite DB. Cover the happy path and the 404.
- [ ] **CORS.** Add `CORSMiddleware` (needed if you test in a web browser).

## Phase 2: Frontend
- [ ] **Scaffold.** From the repo root: `npx create-expo-app@latest mobile`. Run `npx expo start`, scan the QR code with Expo Go.
- [ ] **Read the template.** Look at the `app/` folder (Expo Router, file-based routing). Clear out the demo screens.
- [ ] **Static UI.** Build a screen with a hardcoded todo list using `FlatList`, `Text`, `Pressable`, `TextInput`.
  *Concepts: components, props, `useState`, `StyleSheet`.*
- [ ] **API layer.** Create `api.ts` with `getTodos`, `createTodo`, `toggleTodo`, `deleteTodo` using `fetch`. Keep the base URL in one constant. Use your computer's LAN IP, not `localhost`, and run the backend with `fastapi dev --host 0.0.0.0`.
- [ ] **Connect.** Replace hardcoded data with real calls, first using `useEffect` + `useState` to understand what's happening.
- [ ] **Upgrade.** Switch to `@tanstack/react-query` (`useQuery`, `useMutation`) and notice what it removes.
- [ ] **Polish.** Loading and error states, pull-to-refresh, swipe or long-press to delete.

## Phase 3: Stretch goals (pick any)
- [ ] Due dates and priority
- [ ] Users and login (JWT, `expo-secure-store`)
- [ ] Alembic migrations
- [ ] Move to Postgres and deploy the backend (Fly.io or Railway)
- [ ] Build the app with EAS

## Working with Claude Code (no AI-written code)
- Ask it to **explain**: "What does `Depends` do?"
- Paste your code and ask for a **review** or an explanation of an error.
- Ask for **hints**, not answers: "I'm stuck on step 5, point me in the right direction without writing it."
- Ask it to **check your work** against each step before moving on.
