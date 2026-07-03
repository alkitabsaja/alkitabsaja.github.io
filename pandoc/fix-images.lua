function Image(el)
  if el.src:match("^/") then
    el.src = "." .. el.src
  end
  return el
end