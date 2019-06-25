package com.example.dogapiretrofit.ui

import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import com.example.dogapiretrofit.R
import com.example.dogapiretrofit.databinding.ActivityMainBinding
import com.example.dogapiretrofit.viewmodel.DogViewModel

class MainActivity : AppCompatActivity() {

    val binding: ActivityMainBinding by lazy {
        DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding.lifecycleOwner = this
        binding.vm = DogViewModel()
        binding.adapter = DogAdapter(mCallback)
    }

    private val mCallback = object : DogClickCallback {
        override fun onClick(position: Int, url: String) {
            Toast.makeText(applicationContext, url, Toast.LENGTH_SHORT).show()
        }
    }


}
