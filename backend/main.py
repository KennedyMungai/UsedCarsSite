"""The main script for the backend"""
from fastapi import FastAPI
from dotenv import load_dotenv, find_dotenv

ENV = find_dotenv(load_dotenv())