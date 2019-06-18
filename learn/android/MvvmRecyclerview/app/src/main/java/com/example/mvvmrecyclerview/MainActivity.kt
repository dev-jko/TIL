package com.example.mvvmrecyclerview

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.mvvmrecyclerview.databinding.ActivityMainBinding
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding = DataBindingUtil.setContentView<ActivityMainBinding>(this, R.layout.activity_main)

        binding.run {
            lifecycleOwner = this@MainActivity
            vm = ViewModelProviders.of(this@MainActivity).get(LanguageCodeViewModel::class.java)
            rvContent.adapter = Step1Adapter()
        }
    }





}
