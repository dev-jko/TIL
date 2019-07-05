package com.example.tictactoemvp.presenter

interface Presenter {
    fun onCreate()
    fun onPause()
    fun onResume()
    fun onDestroy()
    fun onButtonSelected(row: Int, col: Int)
    fun onResetSelected()
}