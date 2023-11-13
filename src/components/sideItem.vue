<!-- 导航栏模板 -->
<template>
  <div class="item">
    <div class="icon" v-html="iconSvg">
    </div>
    <div class="title">
      <span>
        <slot name="title"></slot>
      </span>
    </div>
  </div>
</template>
<script>
export default {
  props: ["iconSvg"]
}
</script>
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

.item .icon {
  transition: transform 0.2s;
}

.item:hover .icon {
  transform: translateY(-0.25rem);
}

.item:active {
  color: var(--color-theme-blue-1);
}
</style>
