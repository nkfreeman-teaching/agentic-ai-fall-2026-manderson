-- Adjusts the getting-started guides for the PDF build.

-- Relative links work on GitHub but break in a standalone PDF, so point them
-- at the same files in the GitHub repository.
local base = "https://github.com/nkfreeman-teaching/agentic-ai-fall-2026-manderson/blob/main/"

function Link(el)
  local target = el.target
  if target:match("^%a[%w+.-]*:") or target:match("^#") then
    return el
  end
  -- A reader of one guide's PDF who follows the link to the other guide
  -- should land on its PDF, not its markdown page.
  if target == "mac.md" or target == "windows.md" then
    el.target = base .. "getting-started/" .. target:gsub("%.md$", ".pdf")
  elseif target:sub(1, 3) == "../" then
    el.target = base .. target:sub(4)
  else
    el.target = base .. "getting-started/" .. target
  end
  return el
end

-- Pipe tables get automatic column widths, which LaTeX sets as columns that
-- never wrap. Give the first column 35% of the text width and split the rest.
function Table(tbl)
  local n = #tbl.colspecs
  for i, spec in ipairs(tbl.colspecs) do
    local width = (i == 1) and 0.35 or (0.65 / math.max(n - 1, 1))
    if n == 1 then width = 1 end
    tbl.colspecs[i] = {spec[1], width}
  end
  return tbl
end

-- LaTeX will not break a line inside inline code, so a long file path can run
-- past the margin. Allow a line break after each slash or backslash.
local function latex_escape(s)
  local map = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{", ["}"] = "\\}", ["$"] = "\\$", ["&"] = "\\&",
    ["#"] = "\\#", ["%"] = "\\%", ["_"] = "\\_",
    ["~"] = "\\textasciitilde{}", ["^"] = "\\textasciicircum{}",
  }
  return (s:gsub("[\\{}$&#%%_~^]", map))
end

function Code(el)
  if #el.text <= 20 or not el.text:match("[\\/]") then
    return el
  end
  local parts = {}
  for piece, sep in el.text:gmatch("([^\\/]*)([\\/]?)") do
    if piece == "" and sep == "" then break end
    table.insert(parts, latex_escape(piece) .. latex_escape(sep) .. (sep ~= "" and "\\allowbreak{}" or ""))
  end
  return pandoc.RawInline("latex", "\\texttt{" .. table.concat(parts) .. "}")
end

-- Keep the sentence that introduces a code block on the same page as the box.
function Blocks(blocks)
  local out = pandoc.Blocks({})
  for i, block in ipairs(blocks) do
    local next_block = blocks[i + 1]
    if block.t == "Para" and next_block and next_block.t == "CodeBlock" then
      local lines = select(2, next_block.text:gsub("\n", "")) + 1
      out:insert(pandoc.RawBlock("latex", "\\Needspace{" .. (lines + 5) .. "\\baselineskip}"))
    end
    out:insert(block)
  end
  return out
end
