package com.example.mvvmrecyclerview

import androidx.databinding.BindingAdapter
import androidx.recyclerview.widget.RecyclerView

@BindingAdapter("replaceAll")
fun RecyclerView.replaceAll(list: List<Any>?) {
    (this.adapter as Step1Adapter).run {
        replaceAll(list)
        notifyDataSetChanged()
    }

}