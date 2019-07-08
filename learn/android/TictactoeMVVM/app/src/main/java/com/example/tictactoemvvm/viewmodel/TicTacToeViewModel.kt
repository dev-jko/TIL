package com.example.tictactoemvvm.viewmodel

import androidx.databinding.ObservableArrayMap
import androidx.databinding.ObservableField
import androidx.lifecycle.ViewModel
import com.example.tictactoemvvm.model.Board
import com.example.tictactoemvvm.model.Player

class TicTacToeViewModel : ViewModel() {

    private val model: Board by lazy { Board() }
    val cells: ObservableArrayMap<String, String> = ObservableArrayMap()
    val winner: ObservableField<String> = ObservableField()

    fun onButtonSelected(row: Int, col: Int) {
        val playerThatMoved: Player? = model.mark(row, col)
        if (playerThatMoved != null) {
            cells["$row$col"] = playerThatMoved.toString()
            if (model.winner != null) {
                winner.set(model.winner.toString())
            }
        }
    }

    fun onResetSelected() {
        model.restart()
        winner.set(null)
        cells.clear()
    }

}