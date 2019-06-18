package com.example.mvvmrecyclerview

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import kotlinx.android.synthetic.main.language_code_item.view.*

class Step1Adapter : RecyclerView.Adapter<Step1Adapter.ViewHolder>() {

    private val items = mutableListOf<LanguageCode>()

    fun replaceAll(newItems: List<LanguageCode>?) {
        newItems?.let {
            items.clear()
            items.addAll(newItems)
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Step1Adapter.ViewHolder {
        return ViewHolder(parent)
    }

    override fun getItemCount(): Int {
        return items.size
    }

    override fun onBindViewHolder(holder: Step1Adapter.ViewHolder, position: Int) {
        holder.onBindViewHolder(items[position])
    }

    class ViewHolder(parent: ViewGroup) : RecyclerView.ViewHolder(
        LayoutInflater.from(parent.context).inflate(R.layout.language_code_item, parent, false)
    ) {
        fun onBindViewHolder(item: LanguageCode) {
            with(itemView) {
                tvCode.text = item.code
                tvLanguage.text = item.language
            }
        }
    }

}
