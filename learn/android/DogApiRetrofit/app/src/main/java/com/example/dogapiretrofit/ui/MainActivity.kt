package com.example.dogapiretrofit.ui

import android.os.Bundle
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
        binding.vm!!.text.value = "test"
    }
}
