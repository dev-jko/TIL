package com.nadarm.recyclerviewposition

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.RecyclerView
import com.nadarm.recyclerviewposition.databinding.ItemBinding


class MyAdapter : RecyclerView.Adapter<MyAdapter.ViewHolder>() {

    private var itemList: List<String> = emptyList()

    fun refresh(newList: List<String>) {
        this.itemList = newList
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val binding: ItemBinding = DataBindingUtil.inflate(inflater, R.layout.item, parent, false)
        return ViewHolder(binding)
    }

    override fun getItemCount(): Int {
        return this.itemList.size
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(this.itemList[position])
    }


    class ViewHolder(private val binding: ItemBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(text: String) {
            this.binding.textView.text = text
        }
    }
}