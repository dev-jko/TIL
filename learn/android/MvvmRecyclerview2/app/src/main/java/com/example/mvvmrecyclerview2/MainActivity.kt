package com.example.mvvmrecyclerview2

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val myFragment = MyFragment()
        supportFragmentManager.beginTransaction()
            .add(R.id.fragment_container, myFragment, myFragment.tag).commit()
    }


    fun showToast(myData: MyData) {
        Toast.makeText(this, "${myData.name}, ${myData.age}", Toast.LENGTH_LONG).show()
    }
}
