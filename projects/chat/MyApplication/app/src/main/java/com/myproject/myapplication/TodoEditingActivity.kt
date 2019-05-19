package com.myproject.myapplication

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_todo_editing.*

class TodoEditingActivity : AppCompatActivity() {



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_todo_editing)

        val startDate = intent.getSerializableExtra("startDate")
        val endDate = intent.getSerializableExtra("endDate")

        text_view_todo_editing_start_date.text = startDate.toString()

        text_view_todo_editing_end_date.text = endDate.toString()


        linear_layout_todo_editing_start.setOnClickListener {
            val dialog = DatePickerDialogFragment()
            dialog.show(this.supportFragmentManager, "")
        }

        linear_layout_todo_editing_end.setOnClickListener {
            val dialog = DatePickerDialogFragment()
            dialog.show(this.supportFragmentManager, "")
        }

    }
}
