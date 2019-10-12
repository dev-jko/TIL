package com.nadarm.firstmac


import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment

class Blank2Fragment : Fragment() {

    override fun onAttach(context: Context) {
        super.onAttach(context)
        println("${this.javaClass.simpleName} - onAttach(context)")
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        println("${this.javaClass.simpleName} - onCreate")
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        println("${this.javaClass.simpleName} - onCreateView")
        return inflater.inflate(R.layout.fragment_blank2, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        println("${this.javaClass.simpleName} - onViewCreated")
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        println("${this.javaClass.simpleName} - onActivityCreated")
    }

    override fun onStart() {
        super.onStart()
        println("${this.javaClass.simpleName} - onStart")
    }

    override fun onResume() {
        super.onResume()
        println("${this.javaClass.simpleName} - onResume")
    }

    override fun onPause() {
        super.onPause()
        println("${this.javaClass.simpleName} - onPause")
    }

    override fun onStop() {
        super.onStop()
        println("${this.javaClass.simpleName} - onStop")
    }

    override fun onDestroyView() {
        super.onDestroyView()
        println("${this.javaClass.simpleName} - onDestroyView")
    }

    override fun onDestroy() {
        super.onDestroy()
        println("${this.javaClass.simpleName} - onDestroy")
    }

    override fun onDetach() {
        super.onDetach()
        println("${this.javaClass.simpleName} - onDetach")
    }
}
