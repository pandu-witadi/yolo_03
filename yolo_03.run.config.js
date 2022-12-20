module.exports = {
    apps: [
        {
            name: "ml_celery",
            cwd: ".",
            script: "venv/bin/python3",
            args: "-m celery -A ml_celery.index worker --pool=solo",
            watch: false,
            interpreter: "",
            max_memory_restart: "1G"
        },
        {
            name: "ml_api",
            cwd: "./ml_api",
            script: "venv/bin/python3",
            args: "-m uvicorn index:app --host 0.0.0.0 --port 5155",
            watch: false,
            interpreter: "",
            max_memory_restart: "1G"
        },
        {
            name: "ml_client",
            cwd: "./ml_client",
            script: "venv/bin/python3",
            args: "-m uvicorn index:app --host 0.0.0.0 --port 5156",
            watch: false,
            interpreter: "",
            max_memory_restart: "1G"
        }
    ]
}
