program Project1;

{$APPTYPE CONSOLE}

uses
  Math;

var
  k, r, i, n, x: integer;
  found: boolean;

begin
  readln(n);
  Inc(n, n);
  k := Round(Sqrt(n));
  found := false;
  for i := 1 to k - 1 do
  begin
    r := n - i * i - i;
    x := Floor(Sqrt(r));
    if (x * (x + 1) = r) then
    begin
      found := true;
      break;
    end;
  end;
  if (found) then
  begin
    Write('YES');
  end
  else
  begin
    Write('NO');
  end;
end.