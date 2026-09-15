const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "/api";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  let payload = null;

  try {
    payload = await response.json();
  } catch {
    payload = null;
  }

  if (!response.ok) {
    throw new Error(
      payload?.error ||
        payload?.message ||
        `Request failed with status ${response.status}`
    );
  }

  return payload;
}

export async function getHealth() {
  return request("/health");
}

export async function getDiseases() {
  return request("/diseases");
}

export async function predictDisease(disease, features) {
  return request(`/predict/${disease}`, {
    method: "POST",
    body: JSON.stringify(features),
  });
}
