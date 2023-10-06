package com.example.ezapk

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

// flag{43648c93-bb042eb50bb4-a73a-3b5e-aa52}
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val inp = findViewById<EditText>(R.id.et_flag)
        val c = arrayListOf<Int>(150, 33, 57, 233, 205, 237, 171, 96, 57, 41, 167, 1, 226, 74, 200, 91, 36, 209, 247, 174, 118, 32, 52, 201, 83, 184, 25, 119, 98, 231, 57, 6, 0, 176, 16, 76, 177, 37, 30, 51, 50, 115)

        fun enc(input: String): MutableList<Int> {
            val input_a = input.toCharArray().map { it.toInt() }.toMutableList()
            val rand = arrayOfNulls<Int>(42)
            val a = amz(415411)
            var f = rand.none { it == null }
            while(!f) {
                var x = a.nextInt(42)
                while(rand[x] != null){
                    x = a.nextInt(42)
                }
                rand[x] = 1
                var y = a.nextInt(42)
                while(rand[y] != null){
                    y = a.nextInt(42)
                }
                rand[y] = 1
                f = rand.none { it == null }
                val t = input_a[x].xor(input_a[y])
                input_a[x] = input_a[x].xor(t)
                input_a[y] = input_a[y].xor(t)
//                Log.d("x",x.toString())
//                Log.d("y",y.toString())
            }
            a.setSeed(114514)
            for (i in 0..41) {
                val k = a.nextInt(256)
                input_a[i] = a.value(input_a[i], k)
//                Log.d("nor",k.toString())
            }
            return input_a
        }
        findViewById<Button>(R.id.btn_check).setOnClickListener {
            if( inp.text.toString().length != 42 || !(enc(inp.text.toString()).equals(c))) {
                Toast.makeText(this, "Validation failed~", Toast.LENGTH_SHORT).show()
            }
            else{
                Toast.makeText(this, "Verification successful!", Toast.LENGTH_SHORT).show()
            }
        }
    }
}