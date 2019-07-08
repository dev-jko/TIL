package com.example.tictactoemvvm.view

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.ViewModelProviders
import com.example.tictactoemvvm.R
import com.example.tictactoemvvm.databinding.ActivityMainBinding
import com.example.tictactoemvvm.viewmodel.TicTacToeViewModel

class MainActivity : AppCompatActivity() {
    private val TAG = MainActivity::class.java.simpleName
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = DataBindingUtil.setContentView(this, R.layout.activity_main)
        binding.vm = ViewModelProviders.of(this).get(TicTacToeViewModel::class.java)
    }
}
