package com.example.ezapk

import java.util.Random

class amz {
    lateinit var amzz : Random

    constructor() {
        amzz = Random()
    }
    constructor(s: Long) {
        amzz = Random(s)
    }
    fun nextInt(n: Int): Int {
        return amzz.nextInt(n)
    }
    fun setSeed(s: Long) {
        amzz.setSeed(s)
    }
    fun value(a: Int, b: Int): Int {
        // 同或
        return (a.xor(b)).inv().and(255)
    }
}