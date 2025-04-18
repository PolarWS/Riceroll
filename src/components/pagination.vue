<template>
    <div class="pagination" v-if="pageMax > 1">
        <button @click="$emit('pageChange', 1)" :class="{ active: page === 1 }">1</button>
        <button v-if="startPage > 2 && pageMax > maxDisplayPages" @click="$emit('pageChange', Math.max(1, page - 5))"
            :disabled="page === 1">
            ...
        </button>
        <button v-for="pageNumber in pagesToShow" :key="pageNumber" :class="{ active: pageNumber === page }"
            @click="$emit('pageChange', pageNumber)">
            {{ pageNumber }}
        </button>
        <button v-if="endPage < pageMax - 1 && pageMax > maxDisplayPages"
            @click="$emit('pageChange', Math.min(pageMax, page + 5))" :disabled="page === pageMax">
            ...
        </button>
        <button v-if="pageMax != 1" @click="$emit('pageChange', pageMax)" :class="{ active: page === pageMax }">{{
            pageMax }}</button>
    </div>
</template>
<script>
export default {
    props: {
        pageMax: {
            type: Number,
            required: true
        },
        page: {
            type: Number,
            default: 1
        },
        maxDisplayPages: {
            type: Number,
            default: 5
        }
    },
    computed: {
        startPage() {
            if ((this.pageMax - Math.floor((this.maxDisplayPages)) / 2) <= this.page) {
                return this.pageMax - this.maxDisplayPages + 2;
            } else {
                return this.page - Math.floor((this.maxDisplayPages - 2) / 2);
            }
        },
        endPage() {
            if (this.page <= Math.floor((this.maxDisplayPages) / 2)) {
                return this.maxDisplayPages - 1;
            }else if( this.page >= this.pageMax - Math.floor((this.maxDisplayPages) / 2)){
                return this.pageMax - 1;
            } 
            else {
                return this.page + this.maxDisplayPages - 3 - Math.floor((this.maxDisplayPages - 2) / 2);
            }
        },
        pagesToShow() {
            const pages = [];
            for (let i = this.startPage; i <= this.endPage; i++) {
                if (i > 1 && i < this.pageMax) {
                    pages.push(i);
                }
            }
            return pages;
        }
    }
}
</script>

<style scoped>
.pagination {
    display: flex;
    justify-content: center;
    margin-top: 30px;
    margin-bottom: 30px;
    gap: 10px;
}

.pagination button {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 12px;
    color: var(--color-theme-grayscale65);
    border: 1px solid var(--color-theme-grayscale4);
    border-radius: 5px;
    background-color: #fff;
    cursor: pointer;
    user-select: none;
}

@media screen and (max-width: 600px) {
    .pagination button {
        padding: 6px 10px;
    }

    .pagination {
        margin-top: 20px;
        margin-bottom: 20px;
    }
}


.pagination button:disabled {
    cursor: not-allowed;
}

.pagination button.active {
    color: var(--color-theme-blue-3);
    border: 1px solid var(--color-theme-blue-1);
}

.active {
    background-color: #ccc;
}
</style>