# 《Python编程从入门到实践》 中的 Pygame实现

## 调用函数记录

### `pygame.display`

#### `pygame.display.set_mode()`

创建一个名为 `screen` 的窗口（游戏中所有元素都在其中绘制）

```python
screen = pygame.display.set_mode( (1200, 800) )
# 创建一个 1200 * 800 的窗口
# @return Class surface --> 用于显示游戏元素（例：外星人， 飞船）
```

使用：

* `color`

```python
bg_color = (230, 230, 230)      # RGB 指定
screen.fill(bg_color)
```

----

#### `pygame.display.flip()`

重绘屏幕，让最近绘制的屏幕可见（即：绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见）

```python
pygame.display.flip()
# 
```

### `pygame.event`

####  `pygame.event.get()`

事件检测，包含所有键盘事件和鼠标事件

```python
events = pygame.event.get()
# 获得发生的事件信息
# @return list events --> 利用event.type 可以查看事件类型
```

`event.type` 包含事件：

* `pygame.QUIT` 关闭窗口
