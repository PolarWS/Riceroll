<!-- 导航栏模板 -->
<template>
  <div class="item">
    <div class="icon">
      <slot name="icon"></slot>
    </div>
    <div class="title">
      <span>
        <slot name="title"></slot>
      </span>

    </div>
  </div>
</template>
<style scoped>
.icon,
.title {
  display: flex;
  align-items: center;
}

.icon {
  justify-content: center;
}

.title {
  font-size: 1.5rem;
}

.item {
  display: grid;
  grid-template-columns: 1.25fr 2fr;
  width: 100%;
  height: 5rem;
  cursor: pointer;

}

.item:hover {
  font-weight: 600;
}

.item:active {
  color: #74E4FB;
}
</style>
