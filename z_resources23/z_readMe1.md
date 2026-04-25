# setup23

python3 -m venv .venv23
source .venv23/bin/activate
pip install langgraph pymongo mcp sentence-transformers

<!-- *************************************************************************** -->

first install uv
- curl -LsSf https://astral.sh/uv/install.sh | sh

uv add python-dotenv        <!-- to add new libraries ->

`Action          Manual Way (venv + pip)            Modern Way (uv)`
Setup           python -m venv .venv                Automatic
Activation      source .venv/bin/activate           Not required
Installing      pip install -r requirements.txt     uv sync
Running         python main.py                      uv run main.py

<!-- *************************************************************************** -->

uv run python -m grpc_tools.protoc -I. --python_out=./schema --grpc_python_out=./schema agent.proto
- turn that .proto file into Python code so your agent can "speak" the protocol.



uv run python grpc_adapter.py
uv run python mcp_server.py
uv run python main.py

01) type status in terminal3
02) LangGraph (graph23.py) will send a gRPC message to Terminal 1
03) it checks the logic in Terminal 2, and sends the answer back to your screen.