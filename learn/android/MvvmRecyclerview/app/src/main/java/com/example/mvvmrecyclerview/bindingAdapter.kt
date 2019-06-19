package com.example.mvvmrecyclerview

import androidx.databinding.BindingAdapter
import androidx.recyclerview.widget.RecyclerView

@BindingAdapter("replaceAll")
fun RecyclerView.replaceAll(list: List<LanguageCode>?) {
    (this.adapter as Step1Adapter).run {
        replaceAll(list)
        notifyDataSetChanged()
    }

}