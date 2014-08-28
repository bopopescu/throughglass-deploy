#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
import zlib
import sys

from pack_pb2 import Packet

sys.path.append("..")
import rsa

__author__ = 'yowenlove'

g_compress = Packet.COMPRESS_ZIP


def encrypt_rsa(buf, key):
    # return rsa.encrypt(buf, key)
    return buf


def decrypt_rsa(buf, key):
    return rsa.decrypt(buf, key)
    return buf


def encrypt_aes(buf, key):
    return buf


def decrypt_aes(buf, key):
    return buf


def compress_zip(buf):
    return zlib.compress(buf)


def decompress_zip(buf):
    return zlib.decompress(buf)


def compress_7z(buf):
    # TODO: do not support
    return buf


def decompress_7z(buf):
    # TODO: do not support
    return buf


def encode(buf, key, encrypt, cookie='', func_id=0, version=0, uin=0, ret_code=0, device_id=''):
    pkt = Packet()
    pkt.cookie = cookie
    pkt.version = version
    pkt.func_id = func_id
    pkt.uin = uin
    pkt.ret_code = ret_code
    pkt.device_id = device_id
    pkt.crypt_type = encrypt
    pkt.compress = g_compress

    # encrypt
    if pkt.crypt_type == Packet.CRYPT_AES:
        pkt.data = encrypt_aes(buf, key)

    elif pkt.crypt_type == Packet.CRYPT_RSA:
        pkt.data = encrypt_rsa(buf, key)

    else:
        pkt.data = buf

    # compress
    if pkt.compress == Packet.COMPRESS_ZIP:
        pkt.data = compress_zip(pkt.data)

    elif pkt.compress == Packet.COMPRESS_7Z:
        pkt.data = compress_7z(pkt.data)

    return base64.standard_b64encode(pkt.SerializeToString())


def decode(buf, key):
    pkt = Packet()
    pkt.ParseFromString(base64.standard_b64decode(buf))

    # decompress
    if pkt.compress == Packet.COMPRESS_ZIP:
        pkt.data = decompress_zip(pkt.data)

    elif pkt.compress == Packet.COMPRESS_7Z:
        pkt.data = compress_7z(pkt.data)

    # decrypt
    if pkt.crypt_type == Packet.CRYPT_AES:
        pkt.data = decrypt_aes(buf, key)

    elif pkt.crypt_type == Packet.CRYPT_RSA:
        pkt.data = decrypt_rsa(buf, key)

    return pkt


def pre_decode(buf):
    pkt = Packet()
    pkt.ParseFromString(base64.standard_b64decode(buf))
    return pkt