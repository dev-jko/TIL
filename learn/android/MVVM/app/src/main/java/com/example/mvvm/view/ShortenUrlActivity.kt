package com.example.mvvm.view

import android.os.Bundle
import androidx.lifecycle.ViewModelProviders
import com.example.mvvm.R
import com.example.mvvm.databinding.ActivityShortenUrlBinding
import com.example.mvvm.viewmodel.ShortenUrlViewModel
import com.example.mvvm.viewmodel.ShortenUrlViewModelFactory
import org.koin.android.ext.android.inject

class ShortenUrlActivity : BaseActivity<ActivityShortenUrlBinding>(){

    override val layoutResourceId: Int = R.layout.activity_shorten_url

    private val shortenUrlViewModelFactory: ShortenUrlViewModelFactory by inject()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val shortenUrlViewModel = ViewModelProviders.of(this, shortenUrlViewModelFactory).get(ShortenUrlViewModel::class.java)

        shortenUrlViewModel.clickConvert.observe()

    }
}