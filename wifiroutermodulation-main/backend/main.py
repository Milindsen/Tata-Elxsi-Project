"""Vercel ASGI entrypoint for the QoS FastAPI application."""

from qos.main import app

__all__ = ["app"]
