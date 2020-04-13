# coding: utf8
from config import *
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_logger import Logger
import requests