package com.example.helloworld

import android.os.Bundle
import android.support.v4.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

class MyFragment : Fragment() {

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {

//        return super.onCreateView(inflater, container, savedInstanceState)
        return inflater.inflate(R.layout.my_fragment, container, false)
    }
}